"""
add admin user
"""

from yoyo import step

__depends__ = {'20231020_02_UZR6N-add-record-table'}

steps = [
    step('INSERT INTO public."Users"("Id", "Name", "Email", "RoleId", "IsActive", "PasswordHash") SELECT \'89c290f6-1be4-11ee-be56-0242ac120002\', \'Administrator\', \'admin@endocrincentr.ru\', 0, true, \'3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2\' WHERE NOT EXISTS (SELECT "Id" FROM public."Users" WHERE "Id" = \'89c290f6-1be4-11ee-be56-0242ac120002\');')
]
