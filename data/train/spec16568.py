import numpy as np 

def function(x):

	f4 = x
	r3 = x
	paths = []
	try:
		if r3 >= 7:
			f4 = f4-r3
			paths.append(1)
		else:
			x = f4-6
			paths.append(2)
		if r3 >= 5:
			x = f4*x
			r3 = r3/4
			x = x*x
			paths.append(3)
		else:
			x = x*8
			f4 = 3*x
			f4 = 8*0
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		f4 = r3**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))