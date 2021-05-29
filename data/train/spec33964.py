import numpy as np 

def function(x):

	q5 = 8
	r2 = x
	paths = []
	try:
		if x > 4:
			x = 7/x
			x = q5+x
			x = x*1
			paths.append(1)
		else:
			x = x/1
			x = r2+x
			r2 = r2-x
			paths.append(2)
		if q5 <= 2:
			r2 = 1/6
			q5 = q5/5
			x = x*2
			paths.append(3)
		else:
			q5 = q5/q5
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))