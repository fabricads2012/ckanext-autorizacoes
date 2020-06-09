import ckan.plugins as plugins

"""	
	##########################################################
	# METODOS DE CRIACAO DE OBJETOS CKAN.
	##########################################################
"""
def group_create(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to create groups'}

def group_member_create(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to create group members'}

def member_create(context, data_dict=None):
    return {'success': True}
    #return {'success': True, 'msg': 'No one is allowed to create members'}

def organization_create(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to create organizations'}

def organization_member_create(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to create organization members'}

def related_create(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to create relations'}

def user_create(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to create users'}

"""	
	##########################################################
	# METODOS DE ATUALIZACAO DE OBJETOS CKAN.
	##########################################################
"""
def group_update(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to update groups'}

def organization_update(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to update organizations'}

def package_owner_org_update(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to update package owner'}

def related_update(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to update relations'}

def user_role_bulk_update(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to update users roles'}

def user_role_update(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to update user role'}


"""	
	##########################################################
	# METODOS DE DELECAO DE OBJETOS CKAN.
	##########################################################
"""
def group_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete groups'}

def group_member_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete group members'}

def member_delete(context, data_dict=None):
    return {'success': True}
    #return {'success': False, 'msg': 'No one is allowed to delete members'}

def organization_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete organizations'}

def organization_member_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete organization members'}

def package_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete packages'}

def package_relationship_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete package relationships'}

def related_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete relations'}

def resource_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete resources'}

def tag_delete(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to delete tags'}


"""
	##########################################################
	# METODO SOBRESCRITO DE AUTORIZACAO
	##########################################################

"""
class AutorizacoesPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IAuthFunctions)

    def get_auth_functions(self):
        return {
		# ################### CRIACAO
		'group_create': group_create,
		'group_member_create': group_member_create,
		'member_create': member_create,
		'organization_create': organization_create,
		'organization_member_create': organization_member_create,
		'related_create': related_create,
		'user_create': user_create,
		# ################### ATUALIZACAO
		'group_update': group_update,
		'organization_update': organization_update,
		'package_owner_org_update': package_owner_org_update,
		'related_update': related_update,
		'user_role_bulk_update': user_role_bulk_update,
		'user_role_update': user_role_update,
		# ################### DELECAO
		'group_delete': group_delete,
		'group_member_delete': group_member_delete,
		'member_delete': member_delete,
		'organization_delete': organization_delete,
		'organization_member_delete': organization_member_delete,
		'package_delete': package_delete,
		'package_relationship_delete': package_relationship_delete,
		'related_delete': related_delete,
		'resource_delete': resource_delete,
		'tag_delete': tag_delete,
	}
