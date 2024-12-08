# Unit Test Python Class

The **TestCourse.py** file contains unit tests to test functions 
in **Course.py**. 

## Initial Imports

```python
import unittest
from unittest.mock import patch, mock_open
from Course import Course
```

## Test Create Instance of an Object

```python
def test_get_instance(self):
        """
        Test course instantiation without error
        """
        course = Course('Python 100', 3)
        self.assertEqual(course.course_name, 'Python 100')
        self.assertEqual(course.course_credits, 3)
```

## Test Return Value

Call a function that returns a value and test the expected result.

```python
 def test_str_course(self):
        """
        Test the Course string returns correctly
        """
        course = Course('Python 100', 3)
        self.assertEqual(str(course),'Python 100,3')
```

## Test Print Output

### Single Print Statement

```python
 @patch('builtins.print')
    def test_print_course_info(self,mock_print):
        '''
        Test single print course info
        '''
        course = Course('Python 100', 3)
        course.print_course_info()
        mock_print.assert_called_once_with(f'{course.course_name} awards {course.course_credits}')

```

### Multiple Print Statements

```python
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
```

## Test Raise Exception

### Value Error

```python

def test_get_instance_with_error(self):
    """
    Test course instantiation with error that raises exception
    """
    with self.assertRaises(ValueError):
        Course('Python 100', '3')
```

### FileNotFound Exception

```python
def test_file_not_found(self):
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            Course.read_course_data_from_file('nonexistent_file.json')

```

## Test Reading a File

```python
 def test_read_file_success(self):
    mock_file = mock_open(read_data='[{"course_name": "Python 100","course_credits": 5}]')
    with patch('builtins.open', mock_file):
        expected_result = [{"course_name": "Python 100", "course_credits": 5}]
        result = Course.read_course_data_from_file('courses.json')
        self.assertEqual(result, expected_result)

```

## Test Writing a File

```python
 @patch('builtins.open', new_callable=mock_open)
    def test_write_json_to_file(self, mock_file):
        data = [{"firstName": "Bob", "lastName": "Brown", "reviewDate": "2024-12-02", "reviewRating": 4}]
        filename = 'test.json'
        Course.write_course_data_to_file(data,filename)
        mock_file.assert_called_once_with(filename, 'w')

```