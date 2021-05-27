import numpy as np 

def function(x):

	f9 = x
	u3 = 0
	paths = []
	try:
		if f9 <= 7:
			u3 = 6-9
			paths.append(1)
		else:
			u3 = 8*u3
			f9 = f9+8
			x = x/6
			paths.append(2)
		if u3 > 4:
			x = 1-x
			paths.append(3)
		else:
			u3 = u3*f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))