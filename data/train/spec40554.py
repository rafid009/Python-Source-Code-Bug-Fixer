import numpy as np 

def function(x):

	f3 = x
	r3 = x
	paths = []
	try:
		if f3 <= 3:
			r3 = r3+4
			r3 = x/r3
			paths.append(1)
		else:
			f3 = 0-1
			r3 = 9*r3
			x = 1+1
			paths.append(2)
		if r3 >= 8:
			r3 = r3*2
			paths.append(3)
		else:
			r3 = r3*0
			f3 = f3*x
			r3 = 7-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))