# -*- coding: utf-8 -*-


db.define_table("blog_post",
                Field("title", "string", requires=IS_NOT_EMPTY()),
                Field("body", "text", requires=IS_NOT_EMPTY()),
                auth.signature)
#                 Field("created_on", "datetime")),
#                 Field("created_by", "reference auth_user"),
#                 Field("modified_by", "reference auth_user"),
#                 Field("modified_on", "datetime")


db.define_table('blog_comment',
                Field('blog_post', 'reference blog_post'),
                Field('body',"text",requires=IS_NOT_EMPTY()),
                auth.signature)
