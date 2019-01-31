employee_data = {
    'name': 'Cody Developer',
    'employee_number': 123456,
    'location': {
        'city': 'Minneapolis',
        'office': 'M.123',
        'telephone': '612-123-4567',
    },
    'roles': ['python developer', 'server administrator']
}

# How can you read and modify Cody's office?
# Change cody's office to M.400
employee_data['location']['office'] = 'M.400'

# Print cody's phone number
print(employee_data['location']['telephone'])

# Add a new role for Cody
employee_data['roles'].append('web developer')

# How's everything look?
print(employee_data)


