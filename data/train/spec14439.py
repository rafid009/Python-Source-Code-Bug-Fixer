import numpy as np 

def function(x):

	r3 = 5
	f2 = x
	paths = []
	try:
		if r3 > 2:
			f2 = r3/7
			r3 = 5*r3
			paths.append(1)
		else:
			x = x*9
			x = x/1
			paths.append(2)
		if f2 > 3:
			f2 = f2+f2
			f2 = x+1
			paths.append(3)
		else:
			f2 = 9*f2
			r3 = x+r3
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))