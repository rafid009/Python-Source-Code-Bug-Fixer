import numpy as np 

def function(x):

	r5 = x
	f4 = 3
	paths = []
	try:
		if x <= 8:
			x = x+x
			x = 9*x
			paths.append(1)
		else:
			r5 = r5/2
			paths.append(2)
		if x <= 5:
			r5 = 7/x
			r5 = r5-4
			f4 = 7/1
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		f4 = r5**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))