"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from graphene_django.utils.testing import GraphQLTestCase

from seed.tests.util_test import fill_test_database

class TestGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        fill_test_database()
    
    def test_query_projects(self):
        response_01 = self.query(
            '''
            {
                projects(query: "id=1", orderBy: "id", limit: 1){
                    id
                    name
                    members {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["projects"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                projects{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["projects"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                projectPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    projects { id }
                }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["projectPagination"]["totalPages"], 1)
            self.assertEqual(res_03["projectPagination"]["totalCount"], 1)
            self.assertEqual(res_03["projectPagination"]["projects"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                projectCount(query: "id=1"){ count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["projectCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                projectCount { count }
            }
            ''')
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["projectCount"]["count"], 1)

    def test_query_project(self):
        response = self.query(
            '''
            {
                project(id: 1){
                    id
                    name
                    members {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["project"]["id"], 1)
    
    def test_save_project(self):
        response = self.query(
            '''
            mutation {
                saveProject(
                    name: "",
                    members:  1,
                ) {
                    project {
                        id
                        name
                        members {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveProject"]["project"]["id"], 2)
    
    def test_set_project(self):
        response = self.query(
            '''
            mutation {
                setProject(id:1
                    name: "",
                    members:  1,

                ) {
                    project {
                        id
                        name
                        members {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setProject"]["project"]["id"], 1)
    
    def test_delete_project(self):
        response = self.query(
            '''
            mutation {
                deleteProject(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteProject"]["id"], 1)

    def test_query_tasks(self):
        response_01 = self.query(
            '''
            {
                tasks(query: "id=1", orderBy: "id", limit: 1){
                    id
                    name
                    deadline
                    status
                    assigned {
                      id
                    }
                    project {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["tasks"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                tasks{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["tasks"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                taskPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    tasks { id }
                }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["taskPagination"]["totalPages"], 1)
            self.assertEqual(res_03["taskPagination"]["totalCount"], 1)
            self.assertEqual(res_03["taskPagination"]["tasks"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                taskCount(query: "id=1"){ count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["taskCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                taskCount { count }
            }
            ''')
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["taskCount"]["count"], 1)

    def test_query_task(self):
        response = self.query(
            '''
            {
                task(id: 1){
                    id
                    name
                    deadline
                    status
                    assigned {
                      id
                    }
                    project {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["task"]["id"], 1)
    
    def test_save_task(self):
        response = self.query(
            '''
            mutation {
                saveTask(
                    name: "",
                    deadline: "2020-01-01T12:00:00+00:00",
                    status: "TODO",
                    assigned:  1,
                    project:  1,
                ) {
                    task {
                        id
                        name
                        deadline
                        status
                        assigned {
                          id
                        }
                        project {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveTask"]["task"]["id"], 2)
    
    def test_set_task(self):
        response = self.query(
            '''
            mutation {
                setTask(id:1
                    name: "",
                    deadline: "2020-01-01T12:00:00+00:00",
                    status: "TODO",
                    assigned:  1,
                    project:  1,

                ) {
                    task {
                        id
                        name
                        deadline
                        status
                        assigned {
                          id
                        }
                        project {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setTask"]["task"]["id"], 1)
    
    def test_delete_task(self):
        response = self.query(
            '''
            mutation {
                deleteTask(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteTask"]["id"], 1)

    def test_query_users(self):
        response_01 = self.query(
            '''
            {
                users(query: "id=1", orderBy: "id", limit: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    photo {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["users"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                users{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["users"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                userPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    users { id }
                }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["userPagination"]["totalPages"], 1)
            self.assertEqual(res_03["userPagination"]["totalCount"], 1)
            self.assertEqual(res_03["userPagination"]["users"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                userCount(query: "id=1"){ count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["userCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                userCount { count }
            }
            ''')
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["userCount"]["count"], 1)

    def test_query_user(self):
        response = self.query(
            '''
            {
                user(id: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    photo {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["user"]["id"], 1)
    
    def test_save_user(self):
        response = self.query(
            '''
            mutation {
                saveUser(
                    username: "email@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                    photo: 1,
                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                        photo {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveUser"]["user"]["id"], 2)
    
    def test_set_user(self):
        response = self.query(
            '''
            mutation {
                setUser(id:1
                    username: "email_1@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email_1@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                    photo: 1,

                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                        photo {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setUser"]["user"]["id"], 1)
    
    def test_delete_user(self):
        response = self.query(
            '''
            mutation {
                deleteUser(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteUser"]["id"], 1)