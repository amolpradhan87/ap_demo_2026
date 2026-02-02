"""
User Service Module
Provides discount calculations based on user age and country
"""
# initial version of discount calculation logic

class UserService:
    # Country-based discount rates (in percentage)
    COUNTRY_DISCOUNTS = {
        'US': 5,
        'UK': 7,
        'CA': 6,
        'DE': 8,
        'FR': 8,
        'AU': 6,
        'IN': 10,
        'BR': 12,
        'JP': 5,
    }
    
    # Age-based discount threshold
    SENIOR_AGE = 60
    SENIOR_DISCOUNT = 10
    
    def __init__(self, user_id, age, country):
        """
        Initialize user service
        
        Args:
            user_id: Unique user identifier
            age: User's age
            country: User's country code (e.g., 'US', 'UK')
        """
        self.user_id = user_id
        self.age = age
        self.country = country.upper()
    
    def get_discount(self):
        """
        Calculate total discount for the user
        
        Returns:
            dict: Contains breakdown of discounts and total
        """
        age_discount = 0
        country_discount = 0
        
        # Check age-based discount
        if self.age > self.SENIOR_AGE:
            age_discount = self.SENIOR_DISCOUNT
        
        # Check country-based discount
        if self.country in self.COUNTRY_DISCOUNTS:
            country_discount = self.COUNTRY_DISCOUNTS[self.country]
        
        # Total discount (can be cumulative or max - using cumulative here)
        total_discount = age_discount + country_discount
        
        return {
            'user_id': self.user_id,
            'age_discount': age_discount,
            'country_discount': country_discount,
            'total_discount': total_discount,
            'discount_percentage': f"{total_discount}%"
        }
    
    def apply_discount(self, original_price):
        """
        Apply discount to a price
        
        Args:
            original_price: Original price before discount
            
        Returns:
            dict: Price breakdown with discount applied
        """
        discount_info = self.get_discount()
        total_discount_rate = discount_info['total_discount'] / 100
        discount_amount = original_price * total_discount_rate
        final_price = original_price - discount_amount
        
        return {
            'original_price': original_price,
            'discount_rate': discount_info['total_discount'],
            'discount_amount': round(discount_amount, 2),
            'final_price': round(final_price, 2),
            'breakdown': discount_info
        }


# Example usage
if __name__ == "__main__":
    # Example 1: Senior citizen from US
    user1 = UserService(user_id="U001", age=65, country="US")
    print("User 1 (65 years, US):")
    print(user1.get_discount())
    print(user1.apply_discount(100.00))
    print()
    
    # Example 2: Young user from India
    user2 = UserService(user_id="U002", age=25, country="IN")
    print("User 2 (25 years, IN):")
    print(user2.get_discount())
    print(user2.apply_discount(100.00))
    print()
    
    # Example 3: Senior from Brazil
    user3 = UserService(user_id="U003", age=70, country="BR")
    print("User 3 (70 years, BR):")
    print(user3.get_discount())
    print(user3.apply_discount(100.00))