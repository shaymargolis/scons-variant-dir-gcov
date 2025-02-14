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

def wrap_variant_dir(bld):
    def wrapper(variant_dir, orig_dir, **kwargs):
        variant_dir_p = Path(variant_dir)
        orig_dir_p = Path(orig_dir)

        variant_dir_p.mkdir(parents=True, exist_ok=True)
        variant_dir_txt = Path(variant_dir) / "variant_dir.txt"
        variant_dir_txt.write_text(json.dumps({
            "src": str(orig_dir_p.resolve()),
            "dst": str(variant_dir_p.resolve()),
        }))

        return bld(variant_dir, orig_dir, **kwargs)

    return wrapper

obj_bld = env.VariantDir
env.VariantDir = wrap_variant_dir(obj_bld)

env.Append(LINKFLAGS=["--coverage"], CPPFLAGS=['--coverage'])

# Create three variants with different defines
create_variant(env, 'a', 'CONFIG_A')
create_variant(env, 'b', 'CONFIG_B')
create_variant(env, 'c', 'CONFIG_C')
