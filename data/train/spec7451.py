import numpy as np 

def function(x):

	u3 = 7
	t5 = x
	paths = []
	try:
		if t5 < 3:
			x = 8+u3
			u3 = u3+5
			paths.append(1)
		else:
			x = 2/x
			u3 = u3+7
			paths.append(2)
		if u3 >= 1:
			t5 = t5*2
			paths.append(3)
		else:
			u3 = 9/1
			u3 = 0-2
			t5 = 3-u3
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		u3 = t5**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))