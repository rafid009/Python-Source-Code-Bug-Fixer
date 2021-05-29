import numpy as np 

def function(x):

	j5 = 1
	t2 = x
	paths = []
	try:
		if t2 <= 0:
			j5 = j5-9
			paths.append(1)
		else:
			j5 = j5+x
			x = 4-x
			x = x/5
			paths.append(2)
		if j5 >= 3:
			t2 = 1*t2
			paths.append(3)
		else:
			t2 = t2*0
			t2 = 4*t2
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))