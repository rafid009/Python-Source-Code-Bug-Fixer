import numpy as np 

def function(x):

	r9 = x
	m5 = x
	paths = []
	try:
		if x >= 9:
			r9 = r9-0
			x = 5/9
			paths.append(1)
		else:
			r9 = x+9
			paths.append(2)
		if m5 > 6:
			r9 = r9-4
			x = x+x
			r9 = r9-3
			paths.append(3)
		else:
			r9 = x*m5
			r9 = r9-2
			r9 = r9/6
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))