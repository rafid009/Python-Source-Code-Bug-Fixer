import numpy as np 

def function(x):

	f0 = 8
	q6 = 5
	paths = []
	try:
		if f0 > 6:
			x = x+1
			q6 = f0*f0
			paths.append(1)
		else:
			x = x+x
			f0 = 4*0
			paths.append(2)
		if x <= 1:
			q6 = x*x
			paths.append(3)
		else:
			q6 = 1-6
			x = 2*6
			x = 2+f0
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		f0 = q6**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))