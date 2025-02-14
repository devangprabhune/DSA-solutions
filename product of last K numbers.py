class ProductOfNumbers:
    def __init__(self):
        """
        Initialize the object with an empty list and a running product list.
        The running product list will store products up to each position,
        making it efficient to calculate products of last k numbers.
        """
        self.products = [1]  # Start with 1 as it's the multiplicative identity
    
    def add(self, num: int) -> None:
        """
        Append a number to the stream and update running products.
        If the number is 0, reset the products list as all products after 0 will be 0.
        
        Args:
            num: The number to add to the stream
        """
        if num == 0:
            # If we encounter 0, reset the products list
            # This handles the special case where 0 is in the sequence
            self.products = [1]
        else:
            # Multiply the last running product by the new number
            self.products.append(self.products[-1] * num)
    
    def getProduct(self, k: int) -> int:
        """
        Get the product of the last k numbers in the stream.
        
        Args:
            k: Number of last elements to calculate product for
            
        Returns:
            Product of last k numbers, or 0 if there's a 0 in the sequence
        """
        if k >= len(self.products):
            # If k is larger than our products list (excluding the initial 1),
            # it means we encountered a 0 in the sequence
            return 0
        
        # To get product of last k numbers, divide the last running product
        # by the running product k positions before
        return self.products[-1] // self.products[len(self.products) - k - 1]