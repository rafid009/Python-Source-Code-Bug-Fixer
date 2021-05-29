import numpy as np 

def function(x):

	t1 = x
	j8 = x
	paths = []
	try:
		if x > 8:
			t1 = 1-j8
			paths.append(1)
		else:
			t1 = t1*2
			x = 0+x
			j8 = 4*0
			paths.append(2)
		if j8 > 4:
			x = x*2
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))