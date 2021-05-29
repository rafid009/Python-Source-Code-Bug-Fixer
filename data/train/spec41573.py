import numpy as np 

def function(x):

	m5 = 6
	t2 = x
	paths = []
	try:
		if m5 >= 7:
			m5 = t2-7
			m5 = m5+9
			t2 = t2-8
			paths.append(1)
		else:
			t2 = 3/t2
			m5 = m5-x
			t2 = x*m5
			paths.append(2)
		if m5 < 4:
			m5 = m5+8
			x = x-m5
			paths.append(3)
		else:
			m5 = m5/1
			m5 = 9-m5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		t2 = m5**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))