#!/usr/bin/python

##Copy Rights
##GNU

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: gino_test
short_description: This is my first test
version_added: "2.4"
description: 
    - "This is my first module to verify ansible plugin/modue"

options:
    name:
        description:
          - this is a message
        required: true
    new:
        description:
          - Control to demo
        required: true

author:
    - Cheng Hui Lv(@lvlch)
...
'''

EXAMPLES = '''
Original_message:
    description: The original name param that was passed in
    type: str
    returned: always
message:
    description: The output message that the test module generates
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
         name=dict(type='str', required=True),
         new=dict(type='str', required=False, default=False),
    )

    result = dict(
         changed=False,
         original_message='',
         message=''
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    
    if module.check_mode:
        module.exit_json(**result)
    
    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()