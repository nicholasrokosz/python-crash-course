import privileges as p

admin_example = p.Admin('nick','rokosz', 'scottsdale', 23)
print(admin_example.privileges.show_privileges())