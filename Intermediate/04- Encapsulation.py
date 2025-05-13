"""
Python Encapsulation Tutorial

Encapsulation is one of the fundamental OOP concepts that:
1. Bundles data (attributes) and methods that operate on that data
2. Restricts direct access to some components
3. Prevents accidental modification of data

This tutorial covers:
- Public, Protected, and Private attributes
- Getter and Setter methods
- @property decorator
"""

class BankAccount:
    """Demonstrates encapsulation concepts"""
    
    def __init__(self, account_holder, initial_balance=0):
        """
        Public attributes: Can be accessed directly
        Convention: No underscore prefix
        """
        self.account_holder = account_holder
        
        """
        Protected attributes: Should not be accessed directly (but can be)
        Convention: Single underscore prefix
        """
        self._account_number = self._generate_account_number()
        
        """
        Private attributes: Cannot be accessed directly (name mangling)
        Convention: Double underscore prefix
        """
        self.__balance = initial_balance
    
    # Protected method (single underscore)
    def _generate_account_number(self):
        """Should only be used within class or subclasses"""
        import random
        return f"ACCT-{random.randint(100000, 999999)}"
    
    # Public method to access private attribute (getter)
    def get_balance(self):
        """Traditional getter method"""
        return self.__balance
    
    # Public method to modify private attribute (setter)
    def set_balance(self, amount):
        """Traditional setter method with validation"""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
    
    # Using @property decorator for more Pythonic encapsulation
    @property
    def balance(self):
        """Property getter - accessed like attribute"""
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """Property setter - validates before setting"""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
    
    @property
    def account_number(self):
        """Read-only property (no setter)"""
        return self._account_number
    
    def deposit(self, amount):
        """Public method to safely modify balance"""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Public method to safely modify balance"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False


# ===== Demonstration =====

if __name__ == "__main__":
    print("=== Creating Bank Account ===")
    account = BankAccount("John Doe", 1000)
    
    print("\n=== Accessing Public Members ===")
    print(f"Account holder: {account.account_holder}")  # Public - direct access
    
    print("\n=== Accessing Protected Members ===")
    print(f"Account number (shouldn't access directly): {account._account_number}")  # Protected - accessible but shouldn't
    
    print("\n=== Accessing Private Members ===")
    try:
        print(account.__balance)  # Will raise AttributeError
    except AttributeError as e:
        print(f"Error accessing __balance: {e}")
    
    # Accessing private through name mangling (not recommended)
    print(f"Balance through name mangling (hack): {account._BankAccount__balance}")
    
    print("\n=== Using Traditional Getters/Setters ===")
    print(f"Balance via getter: {account.get_balance()}")
    account.set_balance(1500)
    print(f"New balance via getter: {account.get_balance()}")
    
    print("\n=== Using @property Decorator ===")
    print(f"Balance via property: {account.balance}")  # Note no parentheses
    account.balance = 2000  # Calls setter automatically
    print(f"New balance via property: {account.balance}")
    
    print("\n=== Trying to Set Invalid Values ===")
    account.balance = -500  # Will print warning
    
    print("\n=== Read-only Property ===")
    try:
        account.account_number = "NEW-123"  # Will raise AttributeError
    except AttributeError as e:
        print(f"Cannot modify read-only property: {e}")
    
    print("\n=== Safe Operations via Methods ===")
    account.deposit(500)
    print(f"After deposit: {account.balance}")
    account.withdraw(200)
    print(f"After withdrawal: {account.balance}")
    
    print("\n=== Encapsulation Summary ===")
    print("""
Key Concepts:
1. Access Modifiers:
   - Public: No underscore (accessible anywhere)
   - Protected: _single_underscore (accessible but should be treated as private)
   - Private: __double_underscore (name mangling makes it harder to access)

2. Getter/Setter Methods:
   - Traditional way to control access to private attributes
   - Allows validation before setting values

3. @property Decorator:
   - More Pythonic way to implement getters/setters
   - Accessed like attributes but call methods behind the scenes
   - Can make read-only properties by omitting setter

Best Practices:
- Use private attributes (__) for data that shouldn't be modified directly
- Use properties (@property) instead of get_/set_ methods when possible
- Provide clear public methods for safe operations on private data
""")