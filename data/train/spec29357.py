import numpy as np 

def function(x):

	t1 = x
	p3 = x
	paths = []
	try:
		if p3 < 4:
			x = 4*x
			p3 = 3/1
			x = 7/x
			paths.append(1)
		else:
			p3 = p3/4
			t1 = t1*x
			paths.append(2)
		if t1 < 7:
			t1 = t1*1
			x = 4+x
			p3 = 6*2
			paths.append(3)
		else:
			x = x/8
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