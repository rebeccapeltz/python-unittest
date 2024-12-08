import unittest
from unittest.mock import patch, mock_open
from Course import Course


class TestCourseInstantiate(unittest.TestCase):

    def test_get_instance(self):
        """
        Test course instantiation without error
        """
        course = Course('Python 100', 3)
        self.assertEqual(course.course_name, 'Python 100')
        self.assertEqual(course.course_credits, 3)


    def test_get_instance_with_error(self):
        """
        Test course instantiation with error that raises exception
        """
        with self.assertRaises(ValueError):
            Course('Python 100', '3')


    def test_str_course(self):
        """
        Test the Course string returns correctly
        """
        course = Course('Python 100', 3)
        self.assertEqual(str(course),'Python 100,3')

    @patch('builtins.print')
    def test_print_course_info(self,mock_print):
        '''
        Test single print course info
        '''
        course = Course('Python 100', 3)
        course.print_course_info()
        mock_print.assert_called_once_with(f'{course.course_name} awards {course.course_credits}')

    @patch('builtins.print')
    def test_print_course_info_expanded(self,mock_print):
        """
        Test multiple print statements course info
        """
        course = Course('Python 100', 3)
        course.print_course_info_expanded()
        mock_print.assert_has_calls([
            unittest.mock.call(f"Course Name: {course.course_name}"),
            unittest.mock.call(f"Course Credits: {course.course_credits}"),
            ])


    def test_convert_list_of_courses_to_json(self):
        """
        Input a list of courses and get back json(list of dicts)
        """
        courses = []
        courses.append(Course('python 201',5))
        courses.append(Course('python 301', 4))
        json_data = Course.convert_courses_to_json(courses)
        expected_result = [{"course_name":"Python 201","course_credits":5},{"course_name":"Python 301","course_credits":4}]
        self.assertEqual(json_data, expected_result)

    def test_convert_json_to_list_of_courses(self):
        """
        Input a list of courses and get back json(list of dicts)
        """
        json_data = []
        json_data.append({"course_name":"Python 201", "course_credits":5})
        json_data.append({"course_name":"Python 301", "course_credits":4})
        courses = Course.convert_json_to_courses(json_data)
        expected_result = []
        expected_result.append(Course('python 201',5))
        expected_result.append(Course('python 301', 4))
        self.assertEqual([p.course_name for p in courses], [p.course_name for p in expected_result])

    def test_read_file_success(self):
        mock_file = mock_open(read_data='[{"course_name": "Python 100","course_credits": 5}]')
        with patch('builtins.open', mock_file):
            expected_result = [{"course_name": "Python 100", "course_credits": 5}]
            result = Course.read_course_data_from_file('courses.json')
            self.assertEqual(result, expected_result)

    def test_file_not_found(self):
        with patch('builtins.open', mock_open()) as mock_file:
            mock_file.side_effect = FileNotFoundError
            with self.assertRaises(FileNotFoundError):
                Course.read_course_data_from_file('nonexistent_file.json')

    @patch('builtins.open', new_callable=mock_open)
    def test_write_json_to_file(self, mock_file):
        data = [{"firstName": "Bob", "lastName": "Brown", "reviewDate": "2024-12-02", "reviewRating": 4}]
        filename = 'test.json'
        Course.write_course_data_to_file(data,filename)
        mock_file.assert_called_once_with(filename, 'w')


if __name__ == '__main__':
    unittest.main()
