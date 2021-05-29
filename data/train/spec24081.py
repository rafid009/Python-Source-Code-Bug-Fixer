import numpy as np 

def function(x):

	f4 = 7
	o1 = 2
	paths = []
	try:
		if f4 <= 0:
			x = x*2
			paths.append(1)
		else:
			o1 = o1+8
			x = 5+3
			paths.append(2)
		if x < 8:
			o1 = o1+8
			paths.append(3)
		else:
			o1 = f4-x
			f4 = 2*2
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		f4 = o1**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))