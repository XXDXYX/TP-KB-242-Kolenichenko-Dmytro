import unittest
class TestStudentListOperations(unittest.TestCase):
    def setUp(self):
        """Инициализация перед каждым тестом"""
        self.student_list = []
    
    def test_add_element_to_empty_list(self):
        """Тест добавления элемента в пустой список"""
        new_item = {"name": "Alice", "phone": "1234567890", "age": "20", "country": "USA"}
        self.student_list.append(new_item)
        
        self.assertEqual(len(self.student_list), 1)
        self.assertEqual(self.student_list[0]["name"], "Alice")
    
    def test_add_element_with_sorting(self):
        """Тест добавления элемента с сортировкой по имени"""
        self.student_list = [
            {"name": "Bob", "phone": "111", "age": "21", "country": "UK"},
            {"name": "David", "phone": "333", "age": "22", "country": "Canada"}
        ]
        
        # Добавляем Alice - должна быть в начале
        name = "Alice"
        insertPosition = 0
        for item in self.student_list:
            if name > item["name"]:
                insertPosition += 1
            else:
                break
        
        new_item = {"name": "Alice", "phone": "222", "age": "20", "country": "USA"}
        self.student_list.insert(insertPosition, new_item)
        
        self.assertEqual(self.student_list[0]["name"], "Alice")
        self.assertEqual(self.student_list[1]["name"], "Bob")
        self.assertEqual(self.student_list[2]["name"], "David")
    
    def test_delete_existing_element(self):
        """Тест удаления существующего элемента"""
        self.student_list = [
            {"name": "Alice", "phone": "111", "age": "20", "country": "USA"},
            {"name": "Bob", "phone": "222", "age": "21", "country": "UK"}
        ]
        
        name_to_delete = "Alice"
        deletePosition = -1
        
        for item in self.student_list:
            if name_to_delete == item["name"]:
                deletePosition = self.student_list.index(item)
                break
        
        self.assertNotEqual(deletePosition, -1)
        del self.student_list[deletePosition]
        
        self.assertEqual(len(self.student_list), 1)
        self.assertEqual(self.student_list[0]["name"], "Bob")
    
    def test_delete_nonexistent_element(self):
        """Тест удаления несуществующего элемента"""
        self.student_list = [
            {"name": "Alice", "phone": "111", "age": "20", "country": "USA"}
        ]
        
        name_to_delete = "Charlie"
        deletePosition = -1
        
        for item in self.student_list:
            if name_to_delete == item["name"]:
                deletePosition = self.student_list.index(item)
                break
        
        self.assertEqual(deletePosition, -1)
        self.assertEqual(len(self.student_list), 1)
    
    def test_update_element(self):
        """Тест обновления элемента"""
        self.student_list = [
            {"name": "Alice", "phone": "111", "age": "20", "country": "USA"},
            {"name": "David", "phone": "333", "age": "22", "country": "Canada"}
        ]
        
        name_to_update = "Alice"
        deletePosition = -1
        
        for item in self.student_list:
            if name_to_update == item["name"]:
                deletePosition = self.student_list.index(item)
                break
        
        self.assertNotEqual(deletePosition, -1)
        del self.student_list[deletePosition]
        
        # Добавляем обновленный элемент
        new_item = {"name": "Alice", "phone": "999", "age": "25", "country": "Germany"}
        insertPosition = 0
        for item in self.student_list:
            if new_item["name"] > item["name"]:
                insertPosition += 1
            else:
                break
        
        self.student_list.insert(insertPosition, new_item)
        
        self.assertEqual(self.student_list[0]["phone"], "999")
        self.assertEqual(self.student_list[0]["age"], "25")
        self.assertEqual(self.student_list[0]["country"], "Germany")
    
    def test_list_maintains_alphabetical_order(self):
        """Тест сохранения алфавитного порядка"""
        names = ["Charlie", "Alice", "David", "Bob"]
        self.student_list = []
        
        for name in names:
            insertPosition = 0
            for item in self.student_list:
                if name > item["name"]:
                    insertPosition += 1
                else:
                    break
            self.student_list.insert(insertPosition, {"name": name, "phone": "", "age": "", "country": ""})
        
        expected_order = ["Alice", "Bob", "Charlie", "David"]
        actual_order = [item["name"] for item in self.student_list]
        
        self.assertEqual(actual_order, expected_order)
    
    def test_student_dict_structure(self):
        """Тест структуры словаря студента"""
        student = {"name": "Alice", "phone": "1234567890", "age": "20", "country": "USA"}
        
        required_keys = {"name", "phone", "age", "country"}
        self.assertEqual(set(student.keys()), required_keys)
    
    def test_age_conversion_to_int(self):
        """Тест преобразования возраста в целое число"""
        age_str = "20"
        age_int = int(age_str)
        
        self.assertIsInstance(age_int, int)
        self.assertEqual(age_int, 20)
    
    def test_empty_list_print(self):
        """Тест печати пустого списка"""
        self.student_list = []
        output = []
        
        for elem in self.student_list:
            output.append(f"Student name is {elem['name']}, Age is {elem['age']}, Phone is {elem['phone']}, Country is {elem['country']}")
        
        self.assertEqual(len(output), 0)
    
    def test_print_format(self):
        """Тест формата вывода"""
        self.student_list = [
            {"name": "Alice", "phone": "1234567890", "age": 20, "country": "USA"}
        ]
        
        elem = self.student_list[0]
        expected_output = "Student name is Alice, Age is 20, Phone is 1234567890, Country is USA"
        actual_output = f"Student name is {elem['name']}, Age is {elem['age']}, Phone is {elem['phone']}, Country is {elem['country']}"
        
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()