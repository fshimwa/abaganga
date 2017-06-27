# project/profile/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from project import db
from project.decorators import check_confirmed, check_is_admin
from project.email import send_email
from project.profile.models import Profile
from project.user.models import User
from .forms import ProfileForm

################
#### config ####
################

profile_blueprint = Blueprint('profile', __name__, )


################
#### routes ####
################

@profile_blueprint.route('/profileAdd', methods=['GET', 'POST'])
@login_required
@check_confirmed
def profile_add():
    user = User.query.filter_by(email=current_user.email).first()
    profile = Profile.query.filter_by(user_id=user.id).first()
    form = ProfileForm(obj=profile)
    if form.validate_on_submit():
        profile = Profile(
            user=current_user,
            firstName=form.firstName.data,
            lastName=form.lastName.data,
            bio=form.bio.data,
            profilePic=form.profilePic.data,
            occupation=form.occupation.data,
            workPlace=form.workPlace.data,
            levels=form.levels.data,
            country=form.country.data,
            validity=False,
        )
        db.session.add(profile)
        db.session.commit()
        flash('Your profile has been saved.', 'success')
        return redirect(url_for("profile.display"))
    elif form.is_submitted():
        flash(form.errors, 'danger')
    return render_template('profile/register.html', form=form)


@profile_blueprint.route('/profile_edit/<profile_id>', methods=['GET'])
@login_required
def profile_edit(profile_id):
    profile = Profile.query.filter_by(id=profile_id).first()
    form = ProfileForm(obj=profile)
    return render_template('profile/register.html', form=form)


@profile_blueprint.route('/display', methods=['GET'])
@login_required
@check_confirmed
def display():
    user = User.query.filter_by(email=current_user.email).first()
    profile = Profile.query.filter_by(user_id=user.id).first()

    return render_template('profile/profile.html', profile=profile, user=user)


@profile_blueprint.route('/list', methods=['GET'])
@login_required
@check_confirmed
@check_is_admin
def list_all():
    profiles = Profile.query.all()
    return render_template('profile/list.html', profiles=profiles)


@profile_blueprint.route('/profile_view/<profile_id>', methods=['GET'])
@login_required
def profile_view(profile_id):
    profile = Profile.query.filter_by(id=profile_id).first()

    return render_template('profile/profileView.html', profile=profile)


@profile_blueprint.route('/profile_confirm/<profile_id>', methods=['GET'])
@login_required
def profile_confirm(profile_id):
    profile = Profile.query.get(profile_id)
    user_id = profile.user_id
    user = User.query.filter_by(id=user_id).first()
    profile.validity = False
    db.session.commit()
    html = render_template('profile/confirmed.html')
    subject = "Your Membership Has been Confirmed"
    send_email(user.email, subject, html)
    flash('Membership has been Confirmed.', 'success')
    return render_template('profile/profileView.html', profile=profile)


@profile_blueprint.route('/profile_delete/<profile_id>', methods=['GET'])
@login_required
def profile_delete(profile_id):
    profile = Profile.query.get(profile_id)
    user_id = profile.user_id
    user = User.query.filter_by(id=user_id).first()
    profile.validity = False
    db.session.commit()
    # user = User.query.filter_by(id=profile.user_id).first()
    html = render_template('profile/revoke.html')
    subject = "Your Membership Has been revoked"
    send_email(user.email, subject, html)
    flash('Membership has been Revoked. An email has been sent to the member', 'danger')
    return render_template('profile/profileView.html', profile=profile)
