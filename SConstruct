import os
import json
from pathlib import Path

# Define the source file
source_file = 'test.c'
output_program = 'test'

# Create a function that compiles the source with different defines
def create_variant(env, variant, variant_define):
    # Create a variant directory
    variant_dir = env.VariantDir(f"build/{variant}", 'src')
        
    # Compile the source file in the variant directory
    env.Program(
        f"build/{variant}/{output_program}",
        f"build/{variant}/{source_file}",
        CPPDEFINES=[variant_define],
    )
    
    return env

# SCons environment
env = Environment()

env.Append(LINKFLAGS=["--coverage"], CPPFLAGS=['--coverage'])

# Create three variants with different defines
create_variant(env, 'a', 'CONFIG_A')
create_variant(env, 'b', 'CONFIG_B')
create_variant(env, 'c', 'CONFIG_C')
