// k 个排序链表整合成一个排序链表，也就是说有多个输入，一个输出，类似于漏斗一样的概念。
public class MergeKList()
	public ListNode mergeKList(ListNode[] lists){
		PriorityQueue<ListNode> pq=new PriorityQueue<>(new Comparator<ListNode>(){
public int compare(ListNode a,ListNode b){
		return a.val-b.val;
			}
		});
		ListNode ret=null,cur=null;
		for(ListNode node:lists){
		if(null!=node){
			pq.add(node);
			}
		}
		while(!pq.isEmpty()){
		ListNode node=pq.poll();
		if(null==ret){
			ret=cur=node;
		}
		else{
		cur=cur.next=node;
		}
		if(null!=node.next){
		pq.add(node.next);
		}
		}
		return ret;
		}
}