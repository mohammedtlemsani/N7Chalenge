export interface Mail {
    id: number;
    _from: string;
    to: string;
    object: string;
    subject: string;
    content: string;
    date: Date;
    checked: boolean;
}
