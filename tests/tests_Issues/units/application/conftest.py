from unittest.mock import Mock

import pytest

from Issues.application import interfaces


@pytest.fixture(scope='function')
def issue_book_repo(issue_book_with_id_1):
	issue_book_repo = Mock(interfaces.IssueBookRepo)
	issue_book_repo.get_by_id = Mock(return_value=issue_book_with_id_1)
	issue_book_repo.get_all = Mock(return_value=[issue_book_with_id_1,])
	issue_book_repo.get_all_reader = Mock(return_value=[{1: None},])
	return issue_book_repo


@pytest.fixture(scope='function')
def issue_user_repo(issue_user_with_id_1):
	issue_user_repo = Mock(interfaces.IssueUserRepo)
	issue_user_repo.get_by_id = Mock(return_value=issue_user_with_id_1)
	issue_user_repo.get_all = Mock(return_value=[issue_user_with_id_1,])
	issue_user_repo.get_all_reader = Mock(return_value=[{1: None},])
	return issue_user_repo


@pytest.fixture(scope='function')
def actions(action_with_id_1):
	actions = Mock(interfaces.Actions)
	actions.write_actions = Mock(return_value=None)
	actions.get_action = Mock(return_value=action_with_id_1)
	actions.get_actions = Mock(return_value=[action_with_id_1,])
	return actions

