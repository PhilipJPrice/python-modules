classname = "MyClass"
python_code = "print('hello world')"
template = f"""
public class {classname} {{
    public static void main(String[] args) {{
        System.out.println("{python_code}");
    }}
}}"""

print(template)
