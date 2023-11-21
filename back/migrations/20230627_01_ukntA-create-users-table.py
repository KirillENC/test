"""
Create users table
"""

from yoyo import step

__depends__ = {}

steps = [
    step('ALTER DATABASE test SET datestyle TO "ISO, DMY";CREATE TABLE public."Users"("Id" uuid, "Name" character varying, "Email" character varying, "RoleId" integer, "IsActive" boolean, "PasswordHash" character varying, PRIMARY KEY ("Id"));')
]

