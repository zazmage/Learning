# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    form = SQLFORM.factory(Field("your_name", requires=IS_NOT_EMPTY()),
                           Field("birth_date", "date")).process()
    if form.accepted:
        session.flash = "Form accepted"
        redirect(URL("other", vars={"your_name":form.vars.your_name}))
    elif form.errors:
        response.flash = "Form contains errors"
    else:
        response.flash = "Form displayed for the first time"
    return locals()
    #redirect(URL("other", args=[1,4,6], vars={"a":"test", "b2":78}))
    #return "this is page index"
    #session.c = session.get('c',0) + 1
    #message = "c = %s" % session.c
    #return locals()

def other():
    message = "Welcome %s" % request.vars.your_name
    return locals()
    #x = request.args
    #y = request.vars
    #return "this is the other page request.args=%s, request.vars=%s" % (x,SPAN(y))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
