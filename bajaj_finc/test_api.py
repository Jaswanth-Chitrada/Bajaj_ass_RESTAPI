#!/usr/bin/env python3
"""
Test script for the Bajaj Finc API
Tests the /bfhl endpoint with the provided examples
"""

import requests
import json
import sys

# API endpoint (change this to your deployed URL)
BASE_URL = "http://localhost:5000"

def test_api():
    """Test the API with the provided examples"""
    
    # Test cases from the specification
    test_cases = [
        {
            "name": "Example A",
            "data": ["a", "1", "334", "4", "R", "$"],
            "expected_sum": "339",
            "expected_odd": ["1"],
            "expected_even": ["334", "4"],
            "expected_alphabets": ["A", "R"],
            "expected_special": ["$"],
            "expected_concat": "Ra"
        },
        {
            "name": "Example B", 
            "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"],
            "expected_sum": "103",
            "expected_odd": ["5"],
            "expected_even": ["2", "4", "92"],
            "expected_alphabets": ["A", "Y", "B"],
            "expected_special": ["&", "-", "*"],
            "expected_concat": "ByA"
        },
        {
            "name": "Example C",
            "data": ["A", "ABcD", "DOE"],
            "expected_sum": "0",
            "expected_odd": [],
            "expected_even": [],
            "expected_alphabets": ["A", "ABCD", "DOE"],
            "expected_special": [],
            "expected_concat": "EoDdCbAa"
        }
    ]
    
    print("🚀 Testing Bajaj Finc API")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📋 Test {i}: {test_case['name']}")
        print("-" * 30)
        
        # Prepare request
        payload = {"data": test_case["data"]}
        
        try:
            # Make API call
            response = requests.post(f"{BASE_URL}/bfhl", json=payload)
            
            if response.status_code == 200:
                result = response.json()
                
                print(f"✅ Status: {response.status_code}")
                print(f"✅ Success: {result.get('is_success', False)}")
                print(f"✅ User ID: {result.get('user_id', 'N/A')}")
                print(f"✅ Email: {result.get('email', 'N/A')}")
                print(f"✅ Roll Number: {result.get('roll_number', 'N/A')}")
                
                # Test individual components
                tests_passed = 0
                total_tests = 6
                
                # Test sum
                if result.get('sum') == test_case['expected_sum']:
                    print(f"✅ Sum: {result.get('sum')} (expected: {test_case['expected_sum']})")
                    tests_passed += 1
                else:
                    print(f"❌ Sum: {result.get('sum')} (expected: {test_case['expected_sum']})")
                
                # Test odd numbers
                if sorted(result.get('odd_numbers', [])) == sorted(test_case['expected_odd']):
                    print(f"✅ Odd Numbers: {result.get('odd_numbers')}")
                    tests_passed += 1
                else:
                    print(f"❌ Odd Numbers: {result.get('odd_numbers')} (expected: {test_case['expected_odd']})")
                
                # Test even numbers
                if sorted(result.get('even_numbers', [])) == sorted(test_case['expected_even']):
                    print(f"✅ Even Numbers: {result.get('even_numbers')}")
                    tests_passed += 1
                else:
                    print(f"❌ Even Numbers: {result.get('even_numbers')} (expected: {test_case['expected_even']})")
                
                # Test alphabets
                if sorted(result.get('alphabets', [])) == sorted(test_case['expected_alphabets']):
                    print(f"✅ Alphabets: {result.get('alphabets')}")
                    tests_passed += 1
                else:
                    print(f"❌ Alphabets: {result.get('alphabets')} (expected: {test_case['expected_alphabets']})")
                
                # Test special characters
                if sorted(result.get('special_characters', [])) == sorted(test_case['expected_special']):
                    print(f"✅ Special Characters: {result.get('special_characters')}")
                    tests_passed += 1
                else:
                    print(f"❌ Special Characters: {result.get('special_characters')} (expected: {test_case['expected_special']})")
                
                # Test concatenated string
                if result.get('concat_string') == test_case['expected_concat']:
                    print(f"✅ Concatenated String: {result.get('concat_string')}")
                    tests_passed += 1
                else:
                    print(f"❌ Concatenated String: {result.get('concat_string')} (expected: {test_case['expected_concat']})")
                
                print(f"\n📊 Test {i} Results: {tests_passed}/{total_tests} tests passed")
                
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"Response: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection Error: Make sure the API server is running")
            print(f"   Expected URL: {BASE_URL}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            return False
    
    print("\n" + "=" * 50)
    print("🎉 Testing completed!")
    return True

def test_error_cases():
    """Test error handling"""
    print("\n🔍 Testing Error Cases")
    print("-" * 30)
    
    error_tests = [
        {
            "name": "Missing data field",
            "payload": {},
            "expected_status": 400
        },
        {
            "name": "Non-array data",
            "payload": {"data": "not an array"},
            "expected_status": 400
        },
        {
            "name": "Empty data",
            "payload": {"data": []},
            "expected_status": 200
        }
    ]
    
    for test in error_tests:
        print(f"\n📋 Testing: {test['name']}")
        try:
            response = requests.post(f"{BASE_URL}/bfhl", json=test['payload'])
            if response.status_code == test['expected_status']:
                print(f"✅ Status: {response.status_code} (expected: {test['expected_status']})")
            else:
                print(f"❌ Status: {response.status_code} (expected: {test['expected_status']})")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("🧪 Bajaj Finc API Test Suite")
    print("=" * 50)
    
    # Test main functionality
    success = test_api()
    
    if success:
        # Test error cases
        test_error_cases()
    
    print("\n✨ Test suite completed!") 