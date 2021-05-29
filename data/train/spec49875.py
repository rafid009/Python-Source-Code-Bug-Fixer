import numpy as np 

def function(x):

	r5 = x
	f6 = 4
	paths = []
	try:
		if r5 <= 3:
			x = 7*0
			paths.append(1)
		else:
			x = 6+x
			r5 = r5/3
			x = 7+4
			paths.append(2)
		if x < 6:
			x = 5*x
			paths.append(3)
		else:
			f6 = 7-f6
			f6 = 5+f6
			r5 = r5+r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))