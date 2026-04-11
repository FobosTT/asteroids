import pygame
from pygame import Vector2

def apply_asteroids_gravity(entities, strength_multiplier=500.0, max_influence_dist=500.0):
    """
    Applies gravitational pull from all asteroids to all entities.
    Each asteroid's pull strength is proportional to its radius.
    
    Args:
        entities (list): List of objects with .position and .velocity attributes.
        strength_multiplier (float): Scaler for gravity intensity.
        max_influence_dist (float): Distance beyond which an asteroid has no effect.
    """
    # Identify all potential gravity sources (asteroids)
    sources = [e for e in entities if hasattr(e, 'radius') and hasattr(e, 'position')]

    for entity in entities:
        if not hasattr(entity, "velocity") or not hasattr(entity, "position"):
            continue
            
        # Skip if the entity is its own source (prevents self-acceleration)
        # We check identity to avoid issues with objects that might be equal but different instances
        
        for source in sources:
            if entity is source:
                continue

            direction = source.position - entity.position
            distance = direction.length()

            # Only apply gravity if within influence range and not too close (to avoid infinite force)
            if 0 < distance < max_influence_dist:
                # Gravity formula: F = (Strength * SourceRadius) / distance^2
                # We use a simplified version for game physics stability
                force_magnitude = (strength_multiplier * source.radius) / (distance + 100) # +100 to dampen extreme close-range spikes
                
                gravity_vector = direction.normalize() * force_magnitude
                entity.velocity += gravity_vector
