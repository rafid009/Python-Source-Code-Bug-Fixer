import numpy as np 

def function(x):

	t8 = 1
	f4 = x
	paths = []
	try:
		if x > 2:
			x = 8*8
			t8 = t8/6
			paths.append(1)
		else:
			f4 = x*6
			f4 = 5*4
			x = x-4
			paths.append(2)
		if t8 > 1:
			f4 = t8-f4
			t8 = t8+9
			f4 = f4*0
			paths.append(3)
		else:
			t8 = 3/t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))