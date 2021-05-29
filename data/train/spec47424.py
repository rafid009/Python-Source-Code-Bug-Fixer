import numpy as np 

def function(x):

	r7 = x
	f2 = x
	paths = []
	try:
		if x <= 2:
			r7 = f2-r7
			x = 9-x
			f2 = f2/5
			paths.append(1)
		else:
			x = x+2
			f2 = r7-8
			x = 2*x
			paths.append(2)
		if r7 <= 4:
			r7 = x*r7
			r7 = r7+3
			f2 = 4+f2
			paths.append(3)
		else:
			f2 = f2*6
			r7 = r7+f2
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		f2 = r7**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))