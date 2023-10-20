"""
add doctor user
"""

from yoyo import step

__depends__ = {'20231020_03_66XA0-add-admin-user'}

steps = [
    step('INSERT INTO public."Users"("Id", "Name", "Email", "RoleId", "IsActive", "PasswordHash") SELECT \'e074e89e-6f19-11ee-b962-0242ac120002\', \'Doctor\', \'doctor@endocrincentr.ru\', 1, true, \'3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2\' WHERE NOT EXISTS (SELECT "Id" FROM public."Users" WHERE "Id" = \'e074e89e-6f19-11ee-b962-0242ac120002\');')
]
