import numpy as np
from sklearn.neighbors import NearestNeighbors
from optimizer.distance import cosine_similarity
from shop.models import Item  # Adjust import to point to your Item model

def get_product_features(items):
    """
    Extract numerical features for each product (item).
    For now, we'll use 'price' and 'category_id' as features.
    You can extend this function to include more features (e.g., brand, discount_price, etc.).
    """
    return np.array([[item.price, item.category_id] for item in items])

def train_recommendation_model(products):
    """
    Train the recommendation model using NearestNeighbors.
    We use 'cosine' similarity to find similar products based on their features.
    
    :param products: Queryset of all products (items)
    :return: Trained NearestNeighbors model
    """
    # Extract product features
    product_features = get_product_features(products)

    # Initialize the NearestNeighbors model
    model = NearestNeighbors(metric='cosine', algorithm='brute')

    # Train the model on product features
    model.fit(product_features)

    return model

def get_recommendations(user_cart, all_products):
    """
    Get product recommendations based on the items in the user's cart.

    :param user_cart: List of items in the user's cart
    :param all_products: List of all available products
    :return: List of recommended products
    """
    # Convert products to feature vectors
    product_features = get_product_features(all_products)
    
    # Extract features for user cart items
    cart_features = get_product_features(user_cart)

    # Initialize the model
    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(product_features)

    # Find nearest neighbors for each item in the user's cart
    distances, indices = model.kneighbors(cart_features, n_neighbors=5)

    # Flatten the list of indices and remove duplicates
    recommended_indices = np.unique(indices.flatten())

    # Convert recommended indices to Python integers
    recommended_indices = [int(i) for i in recommended_indices]

    # Filter out items already in the cart
    cart_ids = [item.id for item in user_cart]
    recommended_products = [all_products[i] for i in recommended_indices if all_products[i].id not in cart_ids]
    
    return recommended_products
