import numpy as np 

def function(x):

	f9 = x
	a1 = 2
	paths = []
	try:
		if x > 7:
			a1 = 4-1
			paths.append(1)
		else:
			x = x*0
			f9 = 8/6
			paths.append(2)
		if a1 < 3:
			f9 = x+5
			paths.append(3)
		else:
			f9 = 4-f9
			x = 7*x
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