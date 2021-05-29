import numpy as np 

def function(x):

	t5 = 3
	u3 = x
	paths = []
	try:
		if u3 < 8:
			u3 = 2-u3
			paths.append(1)
		else:
			t5 = 6*t5
			t5 = u3+t5
			t5 = 2+9
			paths.append(2)
		if u3 < 9:
			u3 = t5/u3
			u3 = u3-8
			paths.append(3)
		else:
			u3 = 3/9
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		t5 = u3**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))