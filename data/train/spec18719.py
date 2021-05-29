import numpy as np 

def function(x):

	q0 = 7
	f2 = x
	paths = []
	try:
		if x <= 7:
			q0 = 4+1
			q0 = 7+q0
			paths.append(1)
		else:
			f2 = f2/q0
			paths.append(2)
		if f2 > 8:
			x = x+6
			x = x+f2
			q0 = 3-6
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))