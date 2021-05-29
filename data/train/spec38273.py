import numpy as np 

def function(x):

	t9 = x
	f3 = x
	paths = []
	try:
		if t9 > 6:
			x = t9+f3
			paths.append(1)
		else:
			f3 = 4/9
			paths.append(2)
		if x <= 5:
			f3 = f3*f3
			paths.append(3)
		else:
			t9 = 6/f3
			t9 = 2+8
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		f3 = t9**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))