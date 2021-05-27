import numpy as np 

def function(x):

	r8 = x
	t5 = x
	paths = []
	try:
		if x > 5:
			r8 = 2*5
			r8 = t5*7
			paths.append(1)
		else:
			x = t5-x
			t5 = 2-3
			paths.append(2)
		if r8 > 6:
			r8 = 1/r8
			x = x*1
			t5 = t5+5
			paths.append(3)
		else:
			x = 4-7
			r8 = 6-8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))