# -*- coding: utf-8 -*-
db.define_table("test_table",
                Field("name", "string", requires=IS_NOT_EMPTY()),
                Field("description", "string", requires=IS_NOT_EMPTY()))
