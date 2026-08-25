/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int n1=0,n2=0,sum1=0,sum2=0;
    int rev1=0,rev2=0;
    int dig1=0,dig2=0;
    int count1=0,count2=0;
    struct ListNode *temp1=l1;
    struct ListNode *temp2=l2;

    while(temp1!=NULL){
        count1++;
        temp1=temp1->next;

    }
        while(temp2!=NULL){
        count2++;
        temp2=temp2->next;

    }
    temp1=l1;
    temp2=l2;
    while(temp1!=NULL){
        n1=(temp1->val)*pow(10,(count1-1));
        sum1+=n1;
        count1--;
        temp1=temp1->next;
    }
        while(temp2!=NULL){
        n2=(temp2->val)*pow(10,(count2-1));
        sum2+=n2;
        count2--;  
        temp2=temp2->next;
    }
    while(sum1!=0){
        rev1=rev1*10+(sum1%10);
        sum1=sum1/10;
    }
        while(sum2!=0){
        rev2=rev2*10+(sum2%10);
        sum2=sum2/10;
    }
    int output=rev1+rev2;

    if(output == 0)
{
    struct ListNode *req = malloc(sizeof(struct ListNode));
    req->val = 0;
    req->next = NULL;
    return req;
}



    struct ListNode *req=NULL;
        
    struct ListNode *temp=NULL;

    while(output!=0){
        struct ListNode *newnode=malloc(sizeof(struct ListNode));
        newnode->val=output %10;
        newnode->next=NULL;
        
        if(req==NULL){
            req=newnode;
            temp=newnode;
            output=output/10;
        }
        else{
            temp->next=newnode;
            temp=newnode;
            output=output/10;

        }



    }
    return req;


    
    
}#the main issue with this is it may lead to integer overflow;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
struct ListNode *result=NULL;
struct ListNode *temp=NULL;

int val1=0;
int val2=0;
int carry=0;

while(l1!=NULL || l2 != NULL){
    val1=0;
    val2=0;
    if(l1!=NULL){
        val1=l1->val;

    }

    if(l2 != NULL){
        val2=l2->val;
    }

    int sum=val1+val2+carry;
    carry=sum/10;

    struct ListNode *newnode = malloc(sizeof(struct ListNode));
    newnode->val = sum % 10;
    newnode->next = NULL;

    if(result == NULL)
    {
        result = newnode;
        temp = newnode;
    }
    else
    {
        temp->next = newnode;
        temp = newnode;


    }
        if(l1 != NULL)
        l1 = l1->next;

    if(l2 != NULL)
        l2 = l2->next;




}
if(carry != 0)
{
    struct ListNode *newnode = malloc(sizeof(struct ListNode));

    newnode->val = carry;
    newnode->next = NULL;

    temp->next = newnode;
}
return result;

    
    
}
