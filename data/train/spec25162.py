import numpy as np 

def function(x):

	r6 = x
	t5 = x
	paths = []
	try:
		if t5 < 2:
			r6 = r6+3
			paths.append(1)
		else:
			x = x*6
			r6 = r6/5
			r6 = 3+r6
			paths.append(2)
		if r6 >= 2:
			x = 1+x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))