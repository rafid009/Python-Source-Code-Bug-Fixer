import numpy as np 

def function(x):

	l1 = x
	f5 = x
	paths = []
	try:
		if x <= 1:
			f5 = 3*6
			f5 = 9-f5
			f5 = f5*l1
			paths.append(1)
		else:
			f5 = 0*0
			f5 = l1/9
			paths.append(2)
		if f5 > 6:
			x = 9-1
			paths.append(3)
		else:
			x = l1*2
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))