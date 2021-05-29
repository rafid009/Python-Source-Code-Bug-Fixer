import numpy as np 

def function(x):

	t7 = x
	r5 = x
	paths = []
	try:
		if t7 > 4:
			x = t7+t7
			x = t7-0
			paths.append(1)
		else:
			r5 = 3+r5
			paths.append(2)
		if r5 <= 5:
			r5 = r5/7
			paths.append(3)
		else:
			r5 = 4/r5
			t7 = 6+t7
			x = 2+x
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