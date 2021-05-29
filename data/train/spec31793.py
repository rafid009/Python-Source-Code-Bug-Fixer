import numpy as np 

def function(x):

	t7 = x
	j5 = 1
	x = 2
	paths = []
	try:
		if x >= 6:
			x = t7+8
			t7 = 4-t7
			j5 = 1+x
			paths.append(1)
		else:
			t7 = t7+t7
			x = j5/5
			x = x/j5
			paths.append(2)
		if j5 >= 7:
			x = x*0
			t7 = 2-x
			x = x-j5
			paths.append(3)
		else:
			x = t7*x
			j5 = j5-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))